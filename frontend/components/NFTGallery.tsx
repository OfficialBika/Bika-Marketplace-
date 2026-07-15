type NFT={name?:string; rarity?:string; price?:number; image?:string};

export default function NFTGallery({items=[]}:{items:NFT[]}){
 return <div className="nft-gallery grid gap-4">
  {items.map((n,i)=>(
   <article key={i} className="rounded-2xl border p-4">
    {n.image && <img src={n.image} alt={n.name || 'NFT'} />}
    <h3>{n.name}</h3>
    <p>{n.rarity}</p>
    <span>{n.price||0} BKC</span>
   </article>
  ))}
 </div>;
}
