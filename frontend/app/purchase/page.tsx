"use client";

import {useSearchParams} from "next/navigation";
import {useState} from "react";
import {purchaseCharacter} from "@/lib/api";

export default function Page(){
 const params=useSearchParams();
 const character=params.get("character") || "Supreme Character";
 const [status,setStatus]=useState("");

 async function buy(){
  try{
   setStatus("Processing purchase...");
   await purchaseCharacter(character);
   setStatus("Purchase request completed");
  }catch{
   setStatus("Purchase failed. Try again");
  }
 }

 return (
  <main className="market-page">
   <section className="purchase-panel feature-glow">
    <h1>🛒 Purchase Center</h1>
    <h2>{character}</h2>
    <p>Complete marketplace purchase with BKC.</p>
    <button onClick={buy}>CONFIRM PURCHASE</button>
    {status && <p>{status}</p>}
   </section>
  </main>
 );
}
