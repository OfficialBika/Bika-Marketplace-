export type Character = {
 id?: string;
 name: string;
 rarity?: string;
 price?: number;
 image?: string;
};

export type Wallet = {
 balance?: number;
 transactions?: Transaction[];
};

export type Transaction = {
 type?: string;
 amount?: number;
 id?: string;
};

export type Auction = {
 id?: string;
 name?: string;
 bid?: number;
};

export type Trade = {
 id?: string;
 name?: string;
};

const API = process.env.NEXT_PUBLIC_API_URL || "";

async function request<T>(path:string, options?:RequestInit):Promise<T>{
 const res = await fetch(`${API}${path}`, {
  cache:"no-store",
  ...options
 });

 if(!res.ok){
  throw new Error(`API Error ${res.status}`);
 }

 return res.json() as Promise<T>;
}

export function getFeaturedCharacters(){
 return request<{characters:Character[]}>('/characters/featured');
}

export function getCharacters(){
 return request<{characters:Character[]}>('/characters');
}

export function getWallet(){
 return request<Wallet>('/wallet');
}

export function getTransactions(){
 return request<{transactions:Transaction[]}>('/wallet/transactions');
}

export function getTrades(){
 return request<{trades:Trade[]}>('/trades');
}

export function getAuctions(){
 return request<{auctions:Auction[]}>('/auctions');
}

export function purchaseCharacter(id:string){
 return request<{id?:string;purchase_id?:string}>('/purchase',{
  method:'POST',
  headers:{'Content-Type':'application/json'},
  body:JSON.stringify({character_id:id})
 });
}

export function checkPurchaseStatus(id:string){
 return request<{status?:string}>(`/purchase/${id}/status`);
}
