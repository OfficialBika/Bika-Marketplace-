export function getUserId(){
  if(typeof window === "undefined") return null;
  return localStorage.getItem("bika_user_id");
}

export function setUserId(id:string){
  if(typeof window !== "undefined"){
    localStorage.setItem("bika_user_id", id);
  }
}
