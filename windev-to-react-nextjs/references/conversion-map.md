# Carte de conversion globale & exemple complet

Ce document relie UI, logique et données sur un **exemple bout-en-bout**, et donne des pointeurs vers les autres références.

- Langage WLangage → TypeScript : `wlangage-mapping.md`
- Fenêtres/contrôles → composants/routes Next.js : `ui-mapping.md`
- HFSQL → Prisma : `data-mapping.md`

## Exemple bout-en-bout : fenêtre "Fiche Client" WinDev

### Source WinDev (description + extrait WLangage)

Fenêtre `FEN_Fiche_Client` :
- Champs : `EDT_Nom`, `EDT_Email`, `EDT_DateCreation` (lecture seule), `BTN_Enregistrer`, `BTN_Supprimer`.
- Code du bouton `BTN_Enregistrer` (clic) :

```
SI EDT_Nom = "" ALORS
    Erreur("Le nom est obligatoire")
    RETOUR
FIN

Client.Nom = EDT_Nom
Client.Email = EDT_Email

SI Client.IDClient = 0 ALORS
    Client.DateCreation = DateSys()
    HAjoute(Client)
SINON
    HModifie(Client)
FIN

SI HErreur ALORS
    Erreur("Erreur lors de l'enregistrement : " + HErreurInfo())
SINON
    Ferme()
FIN
```

### Conversion proposée

**1. Modèle de données** (`prisma/schema.prisma`, voir `data-mapping.md`) :

```prisma
model Client {
  id           Int      @id @default(autoincrement())
  nom          String   @db.VarChar(100)
  email        String?  @db.VarChar(150)
  dateCreation DateTime @default(now())
}
```

**2. Validation partagée** (`lib/schemas/client.ts`) :

```ts
import { z } from "zod";

export const clientSchema = z.object({
  nom: z.string().min(1, "Le nom est obligatoire"),
  email: z.string().email().optional().or(z.literal("")),
});
export type ClientInput = z.infer<typeof clientSchema>;
```

**3. Server Action** (`app/clients/actions.ts`) — remplace le code du bouton + `HAjoute`/`HModifie` :

```ts
"use server";
import { prisma } from "@/lib/prisma";
import { clientSchema } from "@/lib/schemas/client";
import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";

export async function saveClient(id: number | null, formData: FormData) {
  const parsed = clientSchema.safeParse({
    nom: formData.get("nom"),
    email: formData.get("email"),
  });
  if (!parsed.success) {
    return { error: parsed.error.flatten().fieldErrors };
  }

  if (id === null) {
    await prisma.client.create({
      data: { ...parsed.data, dateCreation: new Date() },
    });
  } else {
    await prisma.client.update({ where: { id }, data: parsed.data });
  }

  revalidatePath("/clients");
  redirect("/clients");
}
```

**4. Page + formulaire** (`app/clients/[id]/page.tsx` + `components/clients/ClientForm.tsx`) — remplace la fenêtre WinDev :

```tsx
// app/clients/[id]/page.tsx
import { prisma } from "@/lib/prisma";
import { ClientForm } from "@/components/clients/ClientForm";
import { notFound } from "next/navigation";

export default async function FicheClientPage({ params }: { params: { id: string } }) {
  const isNew = params.id === "new";
  const client = isNew
    ? null
    : await prisma.client.findUnique({ where: { id: Number(params.id) } });

  if (!isNew && !client) notFound();

  return (
    <div className="p-6 max-w-lg">
      <h1 className="text-xl font-semibold mb-4">
        {isNew ? "Nouveau client" : `Client : ${client!.nom}`}
      </h1>
      <ClientForm id={isNew ? null : client!.id} defaultValues={client ?? undefined} />
    </div>
  );
}
```

```tsx
// components/clients/ClientForm.tsx
"use client";
import { saveClient } from "@/app/clients/actions";

export function ClientForm({
  id,
  defaultValues,
}: {
  id: number | null;
  defaultValues?: { nom: string; email?: string | null; dateCreation?: Date };
}) {
  return (
    <form action={saveClient.bind(null, id)} className="space-y-4">
      <div>
        <label htmlFor="nom" className="block text-sm font-medium">Nom</label>
        <input
          id="nom"
          name="nom"
          defaultValue={defaultValues?.nom}
          className="mt-1 block w-full rounded border px-3 py-2"
          required
        />
      </div>
      <div>
        <label htmlFor="email" className="block text-sm font-medium">Email</label>
        <input
          id="email"
          name="email"
          type="email"
          defaultValue={defaultValues?.email ?? ""}
          className="mt-1 block w-full rounded border px-3 py-2"
        />
      </div>
      {defaultValues?.dateCreation && (
        <p className="text-sm text-gray-500">
          Créé le {new Date(defaultValues.dateCreation).toLocaleDateString("fr-FR")}
        </p>
      )}
      <div className="flex gap-2">
        <button type="submit" className="rounded bg-blue-600 px-4 py-2 text-white">
          Enregistrer
        </button>
      </div>
    </form>
  );
}
```

### Notes de conversion (à signaler à l'utilisateur)

- La validation `EDT_Nom = ""` devient une **double validation** : côté client (`required` + Zod si on passe par React Hook Form) et côté serveur (Zod dans la Server Action) — ne jamais faire confiance uniquement au client.
- `DateSys()` → `new Date()` côté serveur (pas côté client, pour éviter les décalages de fuseau horaire/horloge).
- `HErreur` / `HErreurInfo()` → `try/catch` autour de l'appel Prisma, ou gestion d'erreur Prisma typée (`PrismaClientKnownRequestError`).
- `Ferme()` (fermeture de la fenêtre WinDev après sauvegarde) → `redirect("/clients")` côté serveur après `revalidatePath`.
- Le bouton `BTN_Supprimer` n'a pas été traité ici : suivre le même schéma (Server Action `deleteClient`, confirmation via `<Dialog>` shadcn avant l'appel).

## Cas particuliers fréquents

| Situation WinDev | Approche recommandée |
|---|---|
| Fenêtre avec **plusieurs onglets**, chacun lié à un fichier HFSQL différent | Une route par onglet (parallel routes) ou un seul formulaire avec sections, selon le couplage des données |
| **Table mémorisée / table en mémoire** alimentée par requête puis affichée | `prisma.findMany` côté serveur → `<Table>` ; si filtrage/tri interactif riche, charger côté client via React Query + endpoint API |
| **Champs calculés** affichés dans la fenêtre (ex: total TTC) | Calculer côté serveur (dans la requête ou juste avant le rendu) plutôt que dupliquer la formule côté client, sauf si recalcul live nécessaire (alors dupliquer dans un hook partagé `lib/calculs.ts`) |
| **Procédure globale** appelée depuis plusieurs fenêtres | Fonction partagée dans `lib/`, ou Server Action partagée si elle touche la DB |
| **Droits utilisateurs** (fenêtres/boutons visibles selon profil) | Vérification du rôle côté serveur (middleware Next.js + check dans la page/Server Action), masquage côté client en complément seulement |
| **Impression d'état (WDDoc)** | Génération PDF côté serveur (`@react-pdf/renderer` pour des layouts simples, Puppeteer si l'état HFSQL est complexe/visuel) |

## Quand le contexte projet existe déjà

Si le dépôt contient déjà un `CLAUDE.md`, un `schema.prisma`, ou des composants existants : **lire ces fichiers d'abord** (`view`) et aligner toute nouvelle conversion sur les conventions déjà en place (nommage des modèles, structure de dossiers, design system utilisé) plutôt que d'appliquer aveuglément les exemples ci-dessus.
