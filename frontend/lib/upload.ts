export async function uploadImage(file:File){
 const form = new FormData();
 form.append("file", file);

 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/upload/image`,{
  method:"POST",
  body:form
 });
 return res.json();
}
