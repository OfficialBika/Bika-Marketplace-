export async function checkHealth(){
 const base = process.env.NEXT_PUBLIC_API_URL;
 const res = await fetch(`${base}/health`);
 return res.json();
}
