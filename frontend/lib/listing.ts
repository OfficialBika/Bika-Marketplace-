export async function createListing(data:any){
 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/marketplace/listing`,{
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify(data)
 });
 return res.json();
}
