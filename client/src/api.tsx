const api = async (endpoint: string, config: {}) => {
  try {
    const response = await fetch(`http://localhost:3001/${endpoint}`, config);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response;
  } catch (error) {
    console.error("Error:", error);
    return error;
  }
};

export default api;