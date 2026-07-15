import {useEffect,useState} from 'react';

export function useWallet(address?:string){
 const [balance,setBalance]=useState(0);
 const [connected,setConnected]=useState(false);
 const [loading,setLoading]=useState(false);

 useEffect(()=>{
  if(!address){setConnected(false); setBalance(0); return;}
  const api=process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
  setLoading(true);
  fetch(`${api}/wallet/${address}`)
   .then(r=>r.json())
   .then(d=>{setBalance(d.balance||0); setConnected(true);})
   .catch(()=>{setBalance(0); setConnected(false);})
   .finally(()=>setLoading(false));
 },[address]);

 return {balance, connected, loading};
}
