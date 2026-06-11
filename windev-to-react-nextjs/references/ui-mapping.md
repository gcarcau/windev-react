# Fenêtres / Pages WinDev → Composants & Routes Next.js

## Principe général

Une **fenêtre WinDev** ou une **page WebDev** devient généralement :

- une **route** Next.js (`app/<segment>/page.tsx`) si elle est accessible directement par navigation ;
- ou un **composant** réutilisable (`components/...`) si c'est une fenêtre interne / popup / volet réutilisé dans plusieurs écrans.

| WinDev | Next.js |
|---|---|
| Fenêtre principale (`FEN_Liste_Clients`) | `app/clients/page.tsx` (Server Component par défaut) |
| Fenêtre de détail/édition (`FEN_Fiche_Client`) | `app/clients/[id]/page.tsx` (affichage) + formulaire en Client Component |
| Fenêtre interne (volet réutilisable) | `components/ClientCard.tsx`, importé où nécessaire |
| Fenêtre modale / popup | Composant Client avec un modal du design system (ex: shadcn `<Dialog>`) |
| Menu / barre de navigation | `app/layout.tsx` (layout global) ou `components/Nav.tsx` |
| Onglets (`Cellule à onglets`) | shadcn/ui `<Tabs>` ou Next.js parallel routes si chaque onglet est lourd |

## Contrôles courants

| Contrôle WinDev | Équivalent React/shadcn |
|---|---|
| `Edit` (saisie texte) | `<Input />` (React Hook Form `register`) |
| `Edit` numérique | `<Input type="number" />` avec validation Zod |
| `Combo Box` / `Radio Button` | `<Select>` / `<RadioGroup>` |
| `Case à cocher` | `<Checkbox>` |
| `Table` / `TreeView Table` (zone répétée liée aux données) | shadcn `<Table>` + données via Server Component (fetch direct) ou React Query |
| `Bouton` avec action serveur (sauvegarde, suppression) | `<Button>` déclenchant une **Server Action** (`"use server"`) ou `onClick` → `fetch('/api/...')` |
| `Image` | `next/image` |
| Barre de progression / jauge | composant custom ou shadcn `<Progress>` |
| Champs liés à un fichier de données (« lié à HFSQL ») | Champs contrôlés (`react-hook-form`) initialisés depuis les données chargées (Server Component → props, ou `useQuery`) |
| Validation de saisie (« Saisie obligatoire », masques) | Schéma **Zod**, partagé entre formulaire (client) et API (validation côté serveur) |
| Messages d'erreur (`Erreur(...)`, `Trace(...)`) | Toasts (shadcn `<Toast>`/`sonner`) côté client ; logs serveur (`console.error`/logger) côté API |

## Pattern recommandé pour un écran "Liste + Fiche"

C'est le pattern le plus fréquent dans les applications de gestion WinDev (table de gestion HFSQL → fenêtre liste + fenêtre fiche).

```
app/
└── clients/
    ├── page.tsx              # liste (Server Component, fetch via Prisma ou API)
    ├── [id]/
    │   └── page.tsx          # fiche détail/édition
    └── new/
        └── page.tsx          # création
components/
└── clients/
    ├── ClientsTable.tsx       # table (Client Component si tri/filtre interactif)
    └── ClientForm.tsx         # formulaire (Client Component, react-hook-form + zod)
app/api/
└── clients/
    ├── route.ts               # GET (liste), POST (création)
    └── [id]/route.ts          # GET, PATCH, DELETE
```

### Exemple — liste (Server Component)

```tsx
// app/clients/page.tsx
import { prisma } from "@/lib/prisma";
import { ClientsTable } from "@/components/clients/ClientsTable";

export default async function ClientsPage() {
  const clients = await prisma.client.findMany({ orderBy: { nom: "asc" } });
  return (
    <div className="p-6">
      <h1 className="text-2xl font-semibold mb-4">Clients</h1>
      <ClientsTable clients={clients} />
    </div>
  );
}
```

### Exemple — formulaire (Client Component + Server Action)

```tsx
// components/clients/ClientForm.tsx
"use client";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { saveClient } from "@/app/clients/actions";

const schema = z.object({
  nom: z.string().min(1, "Nom obligatoire"),
  email: z.string().email().optional(),
});
type FormValues = z.infer<typeof schema>;

export function ClientForm({ defaultValues }: { defaultValues?: Partial<FormValues> }) {
  const { register, handleSubmit, formState: { errors } } =
    useForm<FormValues>({ resolver: zodResolver(schema), defaultValues });

  return (
    <form onSubmit={handleSubmit(saveClient)} className="space-y-4">
      <div>
        <label htmlFor="nom">Nom</label>
        <input id="nom" {...register("nom")} className="input" />
        {errors.nom && <p className="text-red-600 text-sm">{errors.nom.message}</p>}
      </div>
      {/* ... autres champs ... */}
      <button type="submit" className="btn-primary">Enregistrer</button>
    </form>
  );
}
```

```ts
// app/clients/actions.ts
"use server";
import { prisma } from "@/lib/prisma";
import { revalidatePath } from "next/cache";

export async function saveClient(data: { nom: string; email?: string }) {
  await prisma.client.create({ data });
  revalidatePath("/clients");
}
```

## Fidélité visuelle

Si une capture d'écran de la fenêtre WinDev d'origine est fournie :

1. Identifier les zones (en-tête, corps, pied, actions) et les reproduire avec le design system choisi (ex: `flex`/`grid` Tailwind).
2. Conserver l'**ordre des champs** et les **libellés** (sauf demande explicite de reformulation).
3. Les boutons d'action WinDev en bas de fenêtre (Valider/Annuler) → boutons alignés à droite, `<Button variant="default">` / `<Button variant="outline">`.
4. Ne pas chercher le pixel-perfect au détriment de la cohérence du design system — signaler les écarts assumés dans la réponse.
