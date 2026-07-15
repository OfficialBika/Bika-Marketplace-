export async function completeOrder(id:string){
 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/orders/${id}/complete`,{
  method:"POST"
 });
 return res.json();
}
