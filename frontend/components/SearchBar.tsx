"use client";

import {useState} from 'react';

export default function SearchBar(){
 const [query,setQuery]=useState('');
 return <input className="rounded-xl border p-3" value={query} onChange={e=>setQuery(e.target.value)} placeholder="Search assets..." />;
}
