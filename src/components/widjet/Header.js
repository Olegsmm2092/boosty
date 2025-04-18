import React from "react";


export function Header (props) {
    return (
        <div>
            <h2 style={{ color: 'rgb(255, 89, 89)' }}>{ props.logo }</h2>
            <p>{ props.data }</p>
            <a href="/">Home</a>
        </div>
    
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