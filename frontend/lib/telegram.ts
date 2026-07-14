export function initTelegram() {
  if (typeof window === 'undefined') return null

  const telegram = (window as any).Telegram?.WebApp

  if (!telegram) return null

  telegram.ready()
  telegram.expand()

  return telegram
}

export function getTelegramInitData() {
  const app = initTelegram()
  return app?.initData || ''
}
