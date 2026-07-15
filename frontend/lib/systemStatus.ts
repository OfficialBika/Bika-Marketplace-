export async function getStatus(){
 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/system/status`);
 return res.json();
}
