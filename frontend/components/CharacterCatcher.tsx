"use client";
import {useEffect,useState} from "react";

type Character={name:string; image?:string; rarity:string; price?:number};

const fallback: Character[] = [
 {name:"Supreme Cell", rarity:"Legendary • Supreme", price:500},
 {name:"Nahida Prime", rarity:"Mythic • Rare", price:800},
 {name:"Changli Flame", rarity:"Ultra Rare", price:1200},
 {name:"Keqing Shadow", rarity:"Epic • Limited", price:650}
];

export default function CharacterCatcher(){
 const [items,setItems]=useState<Character[]>(fallback);
 const [index,setIndex]=useState(0);

 useEffect(()=>{
  fetch(`${process.env.NEXT_PUBLIC_API_URL}/characters/featured`)
   .then(r=>r.json())
   .then(d=>{
    if(d.characters?.length) setItems(d.characters);
   })
   .catch(()=>{});
 },[]);

 useEffect(()=>{
  const timer=setInterval(()=>{
   setIndex(i=>(i+1)%items.length);
  },3500);
  return()=>clearInterval(timer);
 },[items]);

 const c=items[index];

 return (
  <article className="nft catcher feature-glow">
   <div className="image">
    {c.image ? <img src={c.image} alt={c.name}/> : <span>{c.name}</span>}
   </div>
   <h3>{c.name}</h3>
   <p>{c.rarity}</p>
   <b>{c.price || 0} BKC</b>
   <button className="purchase-btn">VIEW CHARACTER</button>
  </article>
 );
}
