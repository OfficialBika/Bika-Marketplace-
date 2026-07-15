import {useEffect,useState} from 'react';

export function useCharacters(){
 const [characters,setCharacters]=useState<any[]>([]);
 const [loading,setLoading]=useState(true);
 const [error,setError]=useState(false);

 useEffect(()=>{
  const api=process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
  fetch(`${api}/characters`)
   .then(r=>{
    if(!r.ok) throw new Error('failed');
    return r.json();
   })
   .then(d=>setCharacters(d.characters||d||[]))
   .catch(()=>{setCharacters([]);setError(true);})
   .finally(()=>setLoading(false));
 },[]);

 return {characters,loading,error};
}
