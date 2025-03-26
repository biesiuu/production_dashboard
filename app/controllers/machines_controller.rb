class MachinesController < ApplicationController
  before_action :set_machine, only: [:show, :edit, :update, :destroy]

 
  def index
    @machines = Machine.all
  end

  
  def show
  end


  def new
    @machine = Machine.new
  end


  def edit
  end

 
  def create
    @machine = Machine.new(machine_params)
    if @machine.save
      redirect_to @machine, notice: 'Maszyna została dodana.'
    else
      render :new, status: :unprocessable_entity
    end
  end


  def update
    if @machine.update(machine_params)
      redirect_to @machine, notice: 'Maszyna została zaktualizowana.'
    else
      render :edit, status: :unprocessable_entity
    end
  end


def destroy
  puts "DEBUG: Próba usunięcia maszyny #{@machine.id}" # Sprawdź w konsoli serwera
  @machine.destroy
  redirect_to machines_url, notice: 'Maszyna została usunięta.'
end

  private


  def set_machine
    @machine = Machine.find(params[:id])
  rescue ActiveRecord::RecordNotFound
    redirect_to machines_path, alert: 'Maszyna nie została znaleziona.'
  end


  def machine_params
    params.require(:machine).permit(:name, :cycle_time, :active)
  end
end
