const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

async function request(path: string, options: RequestInit = {}) {
 const response = await fetch(`${API_URL}${path}`, options);
 if (!response.ok) throw new Error('API request failed');
 return response.json();
}

export const api = {
 health: () => request('/health'),
 marketplace: () => request('/marketplace/features'),
 wallet: (userId: string) => request(`/wallet/balance/${userId}`),
 trade: () => request('/trade/list'),
 auction: () => request('/auction/list'),
 character: (id: string) => request(`/characters/${id}`),
};
