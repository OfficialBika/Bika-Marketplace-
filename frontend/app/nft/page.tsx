"use client";

const items=[
 {name:"Supreme Cell",rarity:"Legendary",price:500},
 {name:"Nahida Prime",rarity:"Mythic",price:800}
];

export default function Page(){
 return <main className="market-page"><h1>NFT Marketplace</h1><div className="grid">{items.map(i=><article key={i.name}><h2>{i.name}</h2><p>{i.rarity}</p><b>{i.price} BKC</b><button>BUY NOW</button></article>)}</div></main>;
}
