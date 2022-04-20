using Terraria;
using Terraria.ID;
using Terraria.ModLoader;
using Terraria.Utilities;

namespace ExampleMod.Items.Accessories
{
	public class ManaHeart : ModItem
	{
		public override void SetStaticDefaults() {
			Tooltip.SetDefault("Heals you by 20 health for every 200 mana consumed.");
		}

		public override void SetDefaults() {
			item.width = 20;
			item.height = 20;
			item.accessory = true;
			item.value = Item.sellPrice(silver: 30);
			item.rare = ItemRarityID.Blue;
		}
		
		public override void UpdateAccessory(Player player, bool hideVisual) {
			//What Happens While Its Equippeds. e.g: player.maxMinions += 1
		}

		public override void AddRecipes() {
			ModRecipe recipe = new ModRecipe(mod);
			recipe.AddIngredient(ItemID.LifeCrystal, 2);
			recipe.AddTile(TileID.Anvils);
			recipe.SetResult(this);
			recipe.AddRecipe();
		}
	}
}
