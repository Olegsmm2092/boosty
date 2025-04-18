import React from "react";
import { NavLink } from "react-router-dom";

export function Header (props) {
    const activeStyle = { color: '#c77979' }
    const devider = " | "
    return (
        <nav>
            <NavLink to="/" exact activeStyle={activeStyle}>Главная </NavLink> {devider}
            <NavLink to="/about" activeStyle={activeStyle}> О сайте</NavLink>
        </nav>
    
    );
}

export function Footer () {
    return (
        <div>
            <p>Copyright: Oleg Sobadov</p>
        </div>
    
    );
}

// export default Header;