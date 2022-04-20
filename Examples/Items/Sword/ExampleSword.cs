using Terraria.ID;
using Terraria.ModLoader;

namespace MoreMobs.Items
{
	public class SlimeySword : ModItem
	{
		public override void SetStaticDefaults() 
		{
			// DisplayName.SetDefault("SlimeySword")
			Tooltip.SetDefault("The Fastest Sword In The World");
		}

		public override void SetDefaults() 
		{
			item.damage = 4;
			item.melee = true;
			item.width = 40;
			item.height = 40;
			item.useTime = 5;
			item.useAnimation = 5;
			item.useStyle = 1;
			item.knockBack = 0;
			item.value = 10000;
			item.rare = 2;
			item.UseSound = SoundID.Item1;
			item.autoReuse = true;
		}

		public override void AddRecipes() 
		{
			ModRecipe recipe = new ModRecipe(mod);
			recipe.AddIngredient(ItemID.Gel, 10);
			recipe.AddTile(TileID.Furnaces);
			recipe.SetResult(this);
			recipe.AddRecipe();
		}
	}
}