"use client";

import {useEffect,useState} from "react";
import {getCharacters,purchaseCharacter} from "@/lib/api";

type Character={id?:string;name:string;rarity:string;price:number};

const fallback:Character[]=[
 {id:"supreme-cell",name:"Supreme Cell",rarity:"Legendary",price:500},
 {id:"nahida-prime",name:"Nahida Prime",rarity:"Mythic",price:800}
];

export default function Page(){
 const [items,setItems]=useState<Character[]>(fallback);
 const [loading,setLoading]=useState(true);

 useEffect(()=>{
  getCharacters()
   .then(data=>{
    if(data?.characters?.length) setItems(data.characters);
   })
   .catch(()=>{})
   .finally(()=>setLoading(false));
 },[]);

 async function buy(id:string){
  await purchaseCharacter(id);
  alert("Purchase request sent");
 }

 return (
  <main className="market-page">
   <h1>🔥 NFT Marketplace</h1>
   {loading && <p>Loading characters...</p>}
   <div className="nft-grid">
    {items.map(i=>(
     <article className="nft" key={i.name}>
      <div className="image">SUPREME</div>
      <h2>{i.name}</h2>
      <p>{i.rarity}</p>
      <b>{i.price} BKC</b>
      <button onClick={()=>buy(i.id || i.name)}>BUY NOW</button>
     </article>
    ))}
   </div>
  </main>
 );
}
