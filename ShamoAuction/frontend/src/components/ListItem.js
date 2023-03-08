import '../stylesheets/ListItem.css';
import React, { useState } from 'react';
import axios from 'axios';


const ListItem = () => {
  const [item, setItem] = useState({
    title: '',
    description: '',
    price: '',
  });

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/api/items', item);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setItem((prevItem) => ({ ...prevItem, [name]: value }));
  };

  return (
    <div className="list-item">
      <h2>List a new item</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="title">Title</label>
        <input
          type="text"
          name="title"
          value={item.title}
          onChange={handleChange}
          required
        />
        <label htmlFor="description">Description</label>
        <textarea
          name="description"
          value={item.description}
          onChange={handleChange}
          required
        />
        <label htmlFor="price">Price</label>
        <input
          type="number"
          name="price"
          value={item.price}
          onChange={handleChange}
          required
        />
        <button type="submit">List Item</button>
      </form>
    </div>
  );
};

export default ListItem;
