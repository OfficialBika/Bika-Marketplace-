"use client";

import {useEffect,useState} from "react";
import Link from "next/link";

type Character={name:string; image?:string; rarity:string; price?:number; id?:string};

const fallback: Character[] = [
 {id:"supreme-cell",name:"Supreme Cell", rarity:"Legendary • Supreme", price:500},
 {id:"nahida-prime",name:"Nahida Prime", rarity:"Mythic • Rare", price:800},
 {id:"changli-flame",name:"Changli Flame", rarity:"Ultra Rare", price:1200},
 {id:"keqing-shadow",name:"Keqing Shadow", rarity:"Epic • Limited", price:650}
];

export default function CharacterCatcher(){
 const [items,setItems]=useState<Character[]>(fallback);
 const [index,setIndex]=useState(0);
 const [loaded,setLoaded]=useState(false);

 useEffect(()=>{
  const url=process.env.NEXT_PUBLIC_API_URL;
  if(!url){
   setLoaded(true);
   return;
  }

  fetch(`${url}/characters/featured`)
   .then(r=>r.json())
   .then(d=>{
    if(Array.isArray(d?.characters) && d.characters.length){
     setItems(d.characters);
    }
   })
   .catch(()=>{})
   .finally(()=>setLoaded(true));
 },[]);

 useEffect(()=>{
  if(items.length < 2) return;

  const timer=setInterval(()=>{
   setIndex(i=>(i+1)%items.length);
  },3500);

  return()=>clearInterval(timer);
 },[items]);

 const c=items[index];

 if(!c){
  return null;
 }

 return (
  <article className="nft catcher feature-glow">
   <div className="image">
    {c.image ? <img src={c.image} alt={c.name}/> : <span>{loaded ? c.name : "Loading..."}</span>}
   </div>
   <h3>{c.name}</h3>
   <p>{c.rarity}</p>
   <b>{c.price || 0} BKC</b>
   <Link className="purchase-btn" href={`/character/${c.id || c.name}`}>
    VIEW CHARACTER
   </Link>
  </article>
 );
}
