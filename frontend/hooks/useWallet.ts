import {useEffect,useState} from 'react';

export function useWallet(address?:string){
 const [balance,setBalance]=useState(0);
 useEffect(()=>{
  if(!address)return;
  const api=process.env.NEXT_PUBLIC_API_URL;
  fetch(`${api}/wallet/${address}`)
   .then(r=>r.json())
   .then(d=>setBalance(d.balance||0))
   .catch(()=>setBalance(0));
 },[address]);
 return {balance};
}
