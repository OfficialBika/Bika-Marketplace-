export async function createOrder(payload:any){
  const base = process.env.NEXT_PUBLIC_API_URL;
  const res = await fetch(`${base}/purchase/`,{
    method:"POST",
    headers:{
      "Content-Type":"application/json"
    },
    body:JSON.stringify(payload)
  });
  return res.json();
}
