import {useEffect,useState} from 'react';

export function useCharacters(){
 const [characters,setCharacters]=useState<any[]>([]);
 const [loading,setLoading]=useState(true);

 useEffect(()=>{
  const api=process.env.NEXT_PUBLIC_API_URL;
  fetch(`${api}/characters`)
   .then(r=>r.json())
   .then(d=>setCharacters(d.characters||d||[]))
   .catch(()=>setCharacters([]))
   .finally(()=>setLoading(false));
 },[]);

 return {characters,loading};
}
