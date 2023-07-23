import { createRouter, createWebHistory } from "vue-router";

const adminRoutes = [
  {
    path: "/login",
    name: "login",
    component: () => import("../components/auth/Login.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../components/auth/Register.vue"),
  },
  {
    path: "/theatres",
    name: "theatre_list",
    component: () => import("../components/admin/TheatreList.vue"),
  },
  {
    path: "/theatres/create",
    name: "create_theatre",
    component: () => import("../components/admin/CreateTheatre.vue"),
  },
  {
    path: "/theatres/:id/edit",
    name: "edit_theatre",
    component: () => import("../components/admin/EditTheatre.vue"),
  },
  {
    path: "/theatres/:id/shows",
    name: "show_list",
    component: () => import("../components/admin/ShowList.vue"),
  },
  {
    path: "/theatres/:id/shows/create",
    name: "create_show",
    component: () => import("../components/admin/CreateShow.vue"),
  },
  {
    path: "/shows/:id/edit",
    name: "edit_show",
    component: () => import("../components/admin/EditShow.vue"),
  },
  {
    path: "/profile",
    name: "profile",
    component: () => import("../components/common/Profile.vue"),
  },
  {
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: () => import("../components/pages/NotFound.vue"),
  },
];

const adminRouter = createRouter({
  history: createWebHistory(),
  routes: adminRoutes,
});

adminRouter.beforeEach((to, from, next) => {
  const publicPages = ["/login", "/register"];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem("user");

  if (authRequired && !loggedIn) {
    next("/login");
  } else {
    next();
  }
});

const userRoutes = [
  {
    path: "/login",
    name: "login",
    component: () => import("../components/auth/Login.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../components/auth/Register.vue"),
  },
  {
    path: "/profile",
    name: "profile",
    component: () => import("../components/common/Profile.vue"),
  },
  {
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: () => import("../components/pages/NotFound.vue"),
  },
];

const userRouter = createRouter({
  history: createWebHistory(),
  routes: userRoutes, // Use 'routes' instead of 'adminRoutes'
});

userRouter.beforeEach((to, from, next) => {
  const publicPages = ["/login", "/register"];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem("user");

  if (authRequired && !loggedIn) {
    next("/login");
  } else {
    next();
  }
});

export { adminRouter, userRouter };
