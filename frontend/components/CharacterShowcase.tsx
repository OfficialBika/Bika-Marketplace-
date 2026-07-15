type Character={
 name?:string;
 image?:string;
 rarity?:string;
 price?:number;
};

export default function CharacterShowcase({items}:{items:Character[]}){
 return (
  <section className="nft-grid">
   {items.map((item,i)=>(
    <article className="nft" key={i}>
      <img src={item.image || "/placeholder.png"} alt={item.name || "character"}/>
      <h3>{item.name}</h3>
      <p>{item.rarity}</p>
      <b>{item.price || 0} BKC</b>
    </article>
   ))}
  </section>
 );
}
