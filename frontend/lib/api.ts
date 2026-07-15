const API = process.env.NEXT_PUBLIC_API_URL || "";

async function request(path:string, options?:RequestInit){
 const res = await fetch(`${API}${path}`, {
  cache:"no-store",
  ...options
 });

 if(!res.ok){
  throw new Error(`API Error ${res.status}`);
 }

 return res.json();
}

export function getFeaturedCharacters(){
 return request('/characters/featured');
}

export function getCharacters(){
 return request('/characters');
}

export function getWallet(){
 return request('/wallet');
}

export function getTrades(){
 return request('/trades');
}

export function getAuctions(){
 return request('/auctions');
}

export function purchaseCharacter(id:string){
 return request('/purchase',{
  method:'POST',
  headers:{'Content-Type':'application/json'},
  body:JSON.stringify({character_id:id})
 });
}
