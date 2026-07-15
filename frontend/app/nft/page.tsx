"use client";

import {useEffect,useState} from "react";
import {getCharacters,purchaseCharacter,type Character} from "@/lib/api";

const fallback:Character[]=[
 {id:"supreme-cell",name:"Supreme Cell",rarity:"Legendary",price:500},
 {id:"nahida-prime",name:"Nahida Prime",rarity:"Mythic",price:800}
];

export default function Page(){
 const [items,setItems]=useState<Character[]>(fallback);
 const [loading,setLoading]=useState(true);
 const [message,setMessage]=useState("");

 useEffect(()=>{
  getCharacters()
   .then(data=>{
    if(data.characters?.length) setItems(data.characters);
   })
   .catch(()=>setMessage("Unable to load characters"))
   .finally(()=>setLoading(false));
 },[]);

 async function buy(id:string){
  try{
   setMessage("Processing purchase...");
   await purchaseCharacter(id);
   setMessage("Purchase request sent");
  }catch{
   setMessage("Purchase failed");
  }
 }

 return (
  <main className="market-page">
   <h1>🔥 NFT Marketplace</h1>
   {loading && <p>Loading characters...</p>}
   {message && <p>{message}</p>}
   <div className="nft-grid">
    {items.map(i=>(
     <article className="nft" key={i.id || i.name}>
      <div className="image">SUPREME</div>
      <h2>{i.name}</h2>
      <p>{i.rarity}</p>
      <b>{i.price || 0} BKC</b>
      <button onClick={()=>buy(i.id || i.name)}>BUY NOW</button>
     </article>
    ))}
   </div>
  </main>
 );
}
