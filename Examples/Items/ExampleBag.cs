using Terraria;
using Terraria.ID;
using Terraria.ModLoader;

namespace ExampleMod.Items
{
	public class ExplorerBag : ModItem
	{
		public override void SetStaticDefaults() {
			DisplayName.SetDefault("Explorer's Bag");
			Tooltip.SetDefault("<right> for goodies!");
		}

		public override void SetDefaults() {
			item.width = 20;
			item.height = 20;
			item.rare = ItemRarityID.Expert;
		}

		public override bool CanRightClick() {
			return true;
		}

		public override void RightClick(Player player) {

		}

		public override void AddRecipes() {
			ModRecipe recipe = new ModRecipe(mod);
			recipe.AddIngredient(ModContent.ItemType<ExampleItem>(), 10);
			a
			recipe.SetResult(this);
			recipe.AddRecipe();
		}
	}
}