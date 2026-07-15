
"use client";
import {useEffect,useState} from "react";

type Character={name:string; image?:string; rarity:string; price?:number};

export default function CharacterCatcher(){
 const [items,setItems]=useState<Character[]>([]);
 const [index,setIndex]=useState(0);

 useEffect(()=>{
  fetch(`${process.env.NEXT_PUBLIC_API_URL}/characters/featured`)
   .then(r=>r.json()).then(d=>setItems(d.characters||[]))
   .catch(()=>{});
 },[]);

 useEffect(()=>{
  const t=setInterval(()=>setIndex(i=>items.length?(i+1)%items.length:0),5000);
  return()=>clearInterval(t);
 },[items]);

 if(!items.length) return <section className="nft">Loading Featured Characters...</section>;
 const c=items[index];
 return <article className="nft catcher">
   <div className="image">{c.image?<img src={c.image} alt={c.name}/>:c.name}</div>
   <h3>{c.name}</h3>
   <p>{c.rarity}</p>
   <b>{c.price||0} BKC</b>
   <button>VIEW</button>
 </article>
}
