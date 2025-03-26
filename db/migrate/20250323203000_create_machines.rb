class CreateMachines < ActiveRecord::Migration[8.0]
  def change
    create_table :machines do |t|
      t.string :name
      t.integer :cycle_time
      t.boolean :active

      t.timestamps
    end
  end
end
