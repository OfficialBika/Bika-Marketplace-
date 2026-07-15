type Character={name?:string; rarity?:string; price?:number; image?:string};

export default function CharacterGrid({items=[]}:{items:Character[]}){
 return <div className="character-grid grid gap-4">
  {items.map((c,i)=><article key={i} className="rounded-2xl border p-4">
    {c.image && <img src={c.image} alt={c.name || 'Character'} />}
    <h3 className="font-bold">{c.name}</h3>
    <p>{c.rarity}</p>
    <span>{c.price||0} BKC</span>
   </article>)}
  </div>;
}
