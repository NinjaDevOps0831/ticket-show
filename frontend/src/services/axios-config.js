import axios from "axios";
import authHeader from "./auth-header";

axios.defaults.headers.common["Authorization"] = authHeader();

export default axios;
