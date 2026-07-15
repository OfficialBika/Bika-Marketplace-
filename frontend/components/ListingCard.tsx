export default function ListingCard({item}:{item:any}){
 return (
  <article className="nft">
   <h3>{item.name || "Character"}</h3>
   <p>{item.rarity || "Supreme"}</p>
   <b>{item.price || 0} BKC</b>
  </article>
 )
}
