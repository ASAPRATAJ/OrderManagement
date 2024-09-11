import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Importujemy style dla paska nawigacyjnego

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="navbar-logo">
                <Link to="/">MyApp</Link> {/* Link do strony głównej */}
            </div>
            <ul className="navbar-links">
                <li><Link to="/">Home</Link></li>
                <li><Link to="/users">Users</Link></li>
                <li><Link to="/users/create">Create User</Link></li>
                <li><Link to="/products">Products</Link></li>
                <li><Link to="/products/create">Create Product</Link></li>
                <li><Link to="/orders">Orders</Link></li>
                <li><Link to="/orders/create">Create Order</Link></li>
                <li><Link to="/login">Login</Link></li>
            </ul>
        </nav>
    );
};

export default Navbar;
