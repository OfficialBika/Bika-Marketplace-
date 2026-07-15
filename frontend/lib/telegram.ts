export function getTelegramUser(){
  if(typeof window === "undefined") return null;
  const tg = (window as any).Telegram?.WebApp;
  return tg?.initDataUnsafe?.user || null;
}

export function initTelegram(){
  if(typeof window === "undefined") return;
  const tg = (window as any).Telegram?.WebApp;
  if(tg){
    tg.ready();
    tg.expand();
  }
}
