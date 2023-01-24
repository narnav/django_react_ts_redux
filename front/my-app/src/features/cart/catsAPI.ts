import { SERVER } from "../../setting";
import axios from "axios";
import { Ctaegory } from "../../models/Category";

export function getAllCategories() {
  return new Promise<{ data: Ctaegory[] }>((resolve) =>
    axios.get(SERVER + "categories/").then((res) => resolve(res))
  );
}
