import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";
import { adminRouter, userRouter } from "./router";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faHome,
  faUser,
  faUserPlus,
  faSignInAlt,
  faSignOutAlt,
} from "@fortawesome/free-solid-svg-icons";

library.add(faHome, faUser, faUserPlus, faSignInAlt, faSignOutAlt);

const app = createApp(App);

const user = store.state.auth.user;

app.use(store);

if (user != null && user.is_admin) app.use(adminRouter);
else app.use(userRouter);

app.component("font-awesome-icon", FontAwesomeIcon);

app.mount("#app");
