export async function getStatus(){
 const base = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
 const res = await fetch(`${base}/system/status`);
 if(!res.ok) throw new Error('System status unavailable');
 return res.json();
}
