<template>
  <div class="container">
    <br />
    <div class="card">
      <div class="card-header">
        <h2>Show List</h2>
      </div>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Name</th>
              <th scope="col">Rate</th>
              <th scope="col">Tags</th>
              <th scope="col">Price</th>
              <th scope="col">Edit</th>
              <th scope="col">Delete</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in showList" :key="index">
              <td>{{ index + 1 }}</td>
              <td>{{ item.name }}</td>
              <td>{{ item.rate }}</td>
              <td>{{ item.tags }}</td>
              <td>{{ item.price }}</td>
              <td>
                <router-link
                  :to="`/shows/${item.id}/edit`"
                  class="btn btn-primary btn-sm"
                >
                  edit
                </router-link>
              </td>
              <td>
                <button
                  class="btn btn-danger btn-sm"
                  @click="handleDelete(item.id)"
                >
                  delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="d-flex flex-row-reverse">
          <router-link
            :to="`/theatres/${this.$route.params.id}/shows/create`"
            class="btn btn-primary"
          >
            Add
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "../../services/axios-config";

export default {
  name: "ShowListComponent",
  data() {
    return {
      showList: [],
    };
  },
  created() {
    const API_URL = `http://localhost:5000/api/shows/theatres/${this.$route.params.id}`;
    axios
      .get(API_URL)
      .then((response) => {
        this.showList = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    handleDelete(show_id) {
      const API_URL = `http://localhost:5000/api/shows/${show_id}`;
      axios
        .delete(API_URL)
        .then(() => {
          axios
            .get(
              `http://localhost:5000/api/shows/theatres/${this.$route.params.id}`
            )
            .then((response) => {
              this.showList = response.data;
            })
            .catch((error) => {
              console.log(error);
            });
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style></style>
