"use client";

import {useState} from 'react';

export default function ThemeSwitcher(){
 const [theme,setTheme]=useState('neon');
 return <button onClick={()=>setTheme(theme==='neon'?'redblue':'neon')}>
   Theme: {theme}
 </button>
}
