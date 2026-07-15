type Character={name?:string; rarity?:string; price?:number};

export default function CharacterGrid({items=[]}:{items:Character[]}){
 return <div className="character-grid">
  {items.map((c,i)=><article key={i}>
   <h3>{c.name}</h3>
   <p>{c.rarity}</p>
   <span>{c.price||0} BKC</span>
  </article>)}
 </div>;
}
