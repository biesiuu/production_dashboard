class ModifyUsersColumns < ActiveRecord::Migration[8.0]
  def change
    # Zmień na null: false jeśli kolumny już istnieją
    change_column_null :users, :first_name, false, 'Tymczasowe'
    change_column_null :users, :last_name, false, 'Nazwisko'
    
    # Dodaj domyślne wartości dla istniejących rekordów
    reversible do |dir|
      dir.up do
        User.where(first_name: nil).update_all(first_name: 'Tymczasowe')
        User.where(last_name: nil).update_all(last_name: 'Nazwisko')
      end
    end
  end
end