type NFT={name?:string; rarity?:string; price?:number};

export default function NFTGallery({items=[]}:{items:NFT[]}){
 return <div className="nft-gallery">
  {items.map((n,i)=><article key={i}><h3>{n.name}</h3><p>{n.rarity}</p><span>{n.price||0} BKC</span></article>)}
 </div>;
}
