export async function getFeaturedCharacters(){
  const base = process.env.NEXT_PUBLIC_API_URL;
  const res = await fetch(`${base}/characters/featured`, {
    cache: "no-store"
  });
  return res.json();
}

export async function createPurchase(data:{
  user_id:string;
  character_id:string;
  amount:number;
}){
  const base = process.env.NEXT_PUBLIC_API_URL;
  const res = await fetch(`${base}/purchase/`, {
    method:"POST",
    headers:{
      "Content-Type":"application/json"
    },
    body:JSON.stringify(data)
  });

  return res.json();
}
