import {useEffect, useState} from "react";

export function useCharacterRotation(items:any[], interval=5000){
  const [index,setIndex] = useState(0);

  useEffect(()=>{
    if(!items.length) return;
    const timer=setInterval(()=>{
      setIndex(v => (v + 1) % items.length);
    }, interval);

    return ()=>clearInterval(timer);
  },[items, interval]);

  return items[index];
}
