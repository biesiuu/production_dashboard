class CreateProductions < ActiveRecord::Migration[8.0]
  def change
    create_table :productions do |t|
      t.datetime :event_at
      t.references :machine, null: false, foreign_key: true
      t.integer :quantity
      t.boolean :good_part

      t.timestamps
    end
  end
end
