export async function adminUpdate(id:string,data:any){
 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/admin/characters/${id}`,{
  method:"PUT",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify(data)
 });
 return res.json();
}
